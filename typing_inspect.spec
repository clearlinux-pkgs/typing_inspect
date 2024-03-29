#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : typing_inspect
Version  : 0.7.1
Release  : 19
URL      : https://files.pythonhosted.org/packages/c3/da/864ce66818e308b38209d4b1ef0585921d28eb07621ba7d905a0e96bcc80/typing_inspect-0.7.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c3/da/864ce66818e308b38209d4b1ef0585921d28eb07621ba7d905a0e96bcc80/typing_inspect-0.7.1.tar.gz
Summary  : Runtime inspection utilities for typing module.
Group    : Development/Tools
License  : MIT
Requires: typing_inspect-license = %{version}-%{release}
Requires: typing_inspect-python = %{version}-%{release}
Requires: typing_inspect-python3 = %{version}-%{release}
Requires: mypy_extensions
Requires: typing_extensions
BuildRequires : buildreq-distutils3
BuildRequires : mypy_extensions
BuildRequires : typing_extensions

%description
Typing Inspect
==============
[![Build Status](https://travis-ci.org/ilevkivskyi/typing_inspect.svg)](https://travis-ci.org/ilevkivskyi/typing_inspect)

%package license
Summary: license components for the typing_inspect package.
Group: Default

%description license
license components for the typing_inspect package.


%package python
Summary: python components for the typing_inspect package.
Group: Default
Requires: typing_inspect-python3 = %{version}-%{release}

%description python
python components for the typing_inspect package.


%package python3
Summary: python3 components for the typing_inspect package.
Group: Default
Requires: python3-core
Provides: pypi(typing_inspect)
Requires: pypi(mypy_extensions)
Requires: pypi(typing_extensions)

%description python3
python3 components for the typing_inspect package.


%prep
%setup -q -n typing_inspect-0.7.1
cd %{_builddir}/typing_inspect-0.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623086501
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/typing_inspect
cp %{_builddir}/typing_inspect-0.7.1/LICENSE %{buildroot}/usr/share/package-licenses/typing_inspect/6d59abdf2e69c2e84d4f92cf54ac844fb1f16d8b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/typing_inspect/6d59abdf2e69c2e84d4f92cf54ac844fb1f16d8b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
