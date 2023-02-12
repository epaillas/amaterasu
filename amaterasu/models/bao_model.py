from cosmoprimo import *

class BAOModel:
    """Base class for BAO models."""

    def __init__(self, redshift):
        """Initialize the model."""
        self.cosmology = Cosmology(engine='class')
        self.redshift = redshift
        self.set_pk_model()

    def set_pk_model(self):
        """Set the power spectrum model."""
        fo = Fourier(self.cosmology, engine='class')
        pk = fo.pk_interpolator().to_1d(z=self.redshift)
        pk_smooth = PowerSpectrumBAOFilter(pk, engine='wallish2018').smooth_pk_interpolator()
        self.pk_smooth = pk_smooth