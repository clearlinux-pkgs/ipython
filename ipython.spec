#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipython
Version  : 7.0.0
Release  : 33
URL      : https://files.pythonhosted.org/packages/cd/d3/7a6b2659932929389a224ff2ba9c576d4f5677eef2b2437cde054e12b4f4/ipython-7.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/cd/d3/7a6b2659932929389a224ff2ba9c576d4f5677eef2b2437cde054e12b4f4/ipython-7.0.0.tar.gz
Summary  : IPython: Productive Interactive Computing
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ipython-bin
Requires: ipython-python3
Requires: ipython-license
Requires: ipython-data
Requires: ipython-man
Requires: ipython-python
Requires: Pygments
Requires: Sphinx
Requires: backcall
Requires: decorator
Requires: ipykernel
Requires: jedi
Requires: pickleshare
Requires: prompt_toolkit
Requires: setuptools
Requires: simplegeneric
Requires: traitlets
BuildRequires : Pygments
BuildRequires : backcall
BuildRequires : buildreq-distutils3
BuildRequires : decorator
BuildRequires : ipykernel
BuildRequires : ipython
BuildRequires : ipython_genutils
BuildRequires : jedi
BuildRequires : jupyter_client
BuildRequires : jupyter_core
BuildRequires : pexpect
BuildRequires : pickleshare
BuildRequires : prompt_toolkit
BuildRequires : ptyprocess
BuildRequires : python-dateutil
BuildRequires : pyzmq
BuildRequires : setuptools
BuildRequires : simplegeneric
BuildRequires : six
BuildRequires : tornado
BuildRequires : traitlets
BuildRequires : wcwidth

%description
IPython provides a rich toolkit to help you make the most out of using Python

%package bin
Summary: bin components for the ipython package.
Group: Binaries
Requires: ipython-data = %{version}-%{release}
Requires: ipython-license = %{version}-%{release}
Requires: ipython-man = %{version}-%{release}

%description bin
bin components for the ipython package.


%package data
Summary: data components for the ipython package.
Group: Data

%description data
data components for the ipython package.


%package license
Summary: license components for the ipython package.
Group: Default

%description license
license components for the ipython package.


%package man
Summary: man components for the ipython package.
Group: Default

%description man
man components for the ipython package.


%package python
Summary: python components for the ipython package.
Group: Default
Requires: ipython-python3 = %{version}-%{release}

%description python
python components for the ipython package.


%package python3
Summary: python3 components for the ipython package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ipython package.


%prep
%setup -q -n ipython-7.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538067094
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/ipython
cp docs/source/about/license_and_copyright.rst %{buildroot}/usr/share/doc/ipython/docs_source_about_license_and_copyright.rst
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
ipython kernel install --prefix %{buildroot}/usr
## install_append end

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

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/ipython/docs_source_about_license_and_copyright.rst

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/ipython.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
