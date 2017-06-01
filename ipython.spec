#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipython
Version  : 6.1.0
Release  : 9
URL      : https://pypi.debian.net/ipython/ipython-6.1.0.tar.gz
Source0  : https://pypi.debian.net/ipython/ipython-6.1.0.tar.gz
Summary  : IPython: Productive Interactive Computing
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear
Requires: ipython-bin
Requires: ipython-python
Requires: ipython-data
Requires: ipython-doc
Requires: Pygments
Requires: decorator
Requires: ipykernel
Requires: jedi
Requires: pickleshare
Requires: prompt_toolkit
Requires: setuptools
Requires: simplegeneric
Requires: traitlets
BuildRequires : Pygments
BuildRequires : decorator
BuildRequires : ipykernel
BuildRequires : ipython
BuildRequires : ipython_genutils
BuildRequires : jedi
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : pbr
BuildRequires : pexpect
BuildRequires : pickleshare
BuildRequires : pip
BuildRequires : prompt_toolkit
BuildRequires : ptyprocess
BuildRequires : python-dateutil
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
%setup -q -n ipython-6.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1496325349
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## make_install_append content
ipython kernel install --prefix %{buildroot}/usr
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iptest
/usr/bin/iptest3
/usr/bin/ipython
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
/usr/lib/python3*/*
