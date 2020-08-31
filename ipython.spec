#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipython
Version  : 7.18.1
Release  : 71
URL      : https://files.pythonhosted.org/packages/ed/c6/2c40e1fc10690dfbe891a948aa1b0dd4890fd2bce9d2eb29c97a84bb0fcb/ipython-7.18.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ed/c6/2c40e1fc10690dfbe891a948aa1b0dd4890fd2bce9d2eb29c97a84bb0fcb/ipython-7.18.1.tar.gz
Summary  : IPython: Productive Interactive Computing
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear
Requires: ipython-bin = %{version}-%{release}
Requires: ipython-data = %{version}-%{release}
Requires: ipython-license = %{version}-%{release}
Requires: ipython-man = %{version}-%{release}
Requires: ipython-python = %{version}-%{release}
Requires: ipython-python3 = %{version}-%{release}
Requires: Pygments
Requires: backcall
Requires: decorator
Requires: jedi
Requires: pexpect
Requires: pickleshare
Requires: prompt_toolkit
Requires: setuptools
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
BuildRequires : nose
BuildRequires : pexpect
BuildRequires : pickleshare
BuildRequires : prompt_toolkit
BuildRequires : ptyprocess
BuildRequires : pytest
BuildRequires : python-dateutil
BuildRequires : pyzmq
BuildRequires : setuptools
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
Provides: pypi(ipython)
Requires: pypi(backcall)
Requires: pypi(decorator)
Requires: pypi(jedi)
Requires: pypi(pexpect)
Requires: pypi(pickleshare)
Requires: pypi(prompt_toolkit)
Requires: pypi(pygments)
Requires: pypi(setuptools)
Requires: pypi(traitlets)

%description python3
python3 components for the ipython package.


%prep
%setup -q -n ipython-7.18.1
cd %{_builddir}/ipython-7.18.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598909318
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipython
cp %{_builddir}/ipython-7.18.1/COPYING.rst %{buildroot}/usr/share/package-licenses/ipython/f8e8135e4c13eb9436ff08f23dbd3362be77a543
cp %{_builddir}/ipython-7.18.1/LICENSE %{buildroot}/usr/share/package-licenses/ipython/68f5a6f2199e7779b637c326af87d70ef6ee6222
cp %{_builddir}/ipython-7.18.1/docs/source/about/license_and_copyright.rst %{buildroot}/usr/share/package-licenses/ipython/7ababbc82643a97634faa381d823f624683844c0
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
/usr/share/package-licenses/ipython/68f5a6f2199e7779b637c326af87d70ef6ee6222
/usr/share/package-licenses/ipython/7ababbc82643a97634faa381d823f624683844c0
/usr/share/package-licenses/ipython/f8e8135e4c13eb9436ff08f23dbd3362be77a543

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ipython.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
