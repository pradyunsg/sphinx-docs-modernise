import nox


@nox.session
def build(session):
    session.install("sphinx == 4.1.2", "sphinxcontrib-websupport")
    session.run("sphinx-build", "doc", "build/docs")


@nox.session
def serve(session):
    session.install("sphinx == 4.1.2", "sphinxcontrib-websupport", "sphinx-autobuild")
    session.run("sphinx-autobuild", "-a", "doc", "build/docs", "--open-browser")
