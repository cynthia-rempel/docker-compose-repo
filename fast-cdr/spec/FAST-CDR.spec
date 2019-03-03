Name:		Fast-CDR
Version:	1.0.8
Release:	2%{?dist}
Summary:	Fast CDR Serialization Library

License:	ASLv2.0
URL:		http://www.eprosima.com
Source0:	https://github.com/eProsima/Fast-CDR/archive/v%{version}.tar.gz

BuildRequires:	cmake
# Patch1: fastcdr-1.0.6-endian.patch
%description
eProsima FastCDR is a C++ library that provides two serialization mechanisms.
One is the standard CDR serialization mechanism, while the other is a faster
implementation that modifies the standard.

%package devel
Summary:	Development files and libraries for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and libraries for %{name}

%prep
%setup -q
# %patch1 -p1 -b .endian~

%build

sed -i 's/.*COMPILE\_LANGUAGE.*//g' cmake/common/check_configuration.cmake

%cmake -DBUILD_SHARED_LIBS=ON \
   -DSECURITY=ON \
   -DBUILD_JAVA=ON \
   -DCOMPILE_EXAMPLES=ON \
   -DBUILD_DOCUMENTATION=ON \
   -DINSTALL_EXAMPLES=ON \
   -DFORCE_CXX=11 \
   -DCMAKE_CXX_STANDARD=11
make %{?_smp_mflags}


%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_libdir}/*.so.*
%{_datadir}/fastcdr/

%files devel
%{_includedir}/fastcdr/
%{_libdir}/*.so
# %{_libdir}/fastcdr/

%changelog
* Sat Jun 10 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-2
- Rename endian define to avoid conflicts

* Fri Jun 9 2017 Rich Mattes <richmattes@gmail.com> - 1.0.6-1
- Initial package
