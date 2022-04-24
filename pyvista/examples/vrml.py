"""VRML examples."""

from .downloads import _retrieve_file

VRML_SAMPLES_ROOT_URL = "https://raw.githubusercontent.com/lorensen/VTKExamples/master"


def _download_file(end_url):
    """Download a vrml example file."""
    basename = end_url.split('/')[-1]
    filename, _ = _retrieve_file(VRML_SAMPLES_ROOT_URL + end_url, basename)
    return filename


def download_teapot():
    """Download the a 2-manifold solid version of the famous teapot example.

    Files hosted at https://github.com/lorensen/VTKExamples/blob/master/src/Testing/Data

    Returns
    -------
    str
        Filename of the VRML file.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> vrml_file = examples.vrml.download_teapot() # doctest:+SKIP
    >>> pl = pyvista.Plotter() # doctest:+SKIP
    >>> pl.import_vrml(vrml_file) # doctest:+SKIP
    >>> pl.show() # doctest:+SKIP

    """
    return _download_file("src/Testing/Data/teapot.wrl")


def download_sextant():
    """Download the sextant example.

    Files hosted at https://github.com/lorensen/VTKExamples/blob/master/src/Testing/Data

    Returns
    -------
    str
        Filename of the VRML file.

    Examples
    --------
    >>> import pyvista
    >>> from pyvista import examples
    >>> vrml_file = examples.vrml.download_sextant() # doctest:+SKIP
    >>> pl = pyvista.Plotter() # doctest:+SKIP
    >>> pl.import_vrml(vrml_file) # doctest:+SKIP
    >>> pl.show() # doctest:+SKIP

    """
    return _download_file("src/Testing/Data/sextant.wrl")
