#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipython
Version  : 5.2.2
Release  : 4
URL      : https://pypi.python.org/packages/6e/cf/c2a3ca5942e2d8084574157a8f818efafb7218204cd9e41166c92c452e07/ipython-5.2.2.tar.gz
Source0  : https://pypi.python.org/packages/6e/cf/c2a3ca5942e2d8084574157a8f818efafb7218204cd9e41166c92c452e07/ipython-5.2.2.tar.gz
Summary  : IPython: Productive Interactive Computing
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear
Requires: ipython-bin
Requires: ipython-python
Requires: ipython-data
Requires: ipython-doc
BuildRequires : Pygments
BuildRequires : decorator
BuildRequires : ipykernel
BuildRequires : ipython
BuildRequires : ipython_genutils
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : pbr
BuildRequires : pexpect
BuildRequires : pickleshare
BuildRequires : pip
BuildRequires : prompt_toolkit
BuildRequires : ptyprocess
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pyzmq
BuildRequires : setuptools
BuildRequires : simplegeneric
BuildRequires : six
BuildRequires : tornado
BuildRequires : traitlets
BuildRequires : wcwidth

%description
.. image:: https://codecov.io/github/ipython/ipython/coverage.svg?branch=master
:target: https://codecov.io/github/ipython/ipython?branch=master

%package bin
Summary: bin components for the ipython package.
Group: Binaries
Requires: ipython-data

%description bin
bin components for the ipython package.


%package data
Summary: data components for the ipython package.
Group: Data

%description data
data components for the ipython package.


%package doc
Summary: doc components for the ipython package.
Group: Documentation

%description doc
doc components for the ipython package.


%package python
Summary: python components for the ipython package.
Group: Default

%description python
python components for the ipython package.


%prep
%setup -q -n ipython-5.2.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487700349
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487700349
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
## make_install_append content
ipython kernel install --prefix %{buildroot}/usr
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iptest
/usr/bin/iptest2
/usr/bin/iptest3
/usr/bin/ipython
/usr/bin/ipython2
/usr/bin/ipython3

%files data
%defattr(-,root,root,-)
/usr/share/jupyter/kernels/python3/kernel.json
/usr/share/jupyter/kernels/python3/logo-32x32.png
/usr/share/jupyter/kernels/python3/logo-64x64.png

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
