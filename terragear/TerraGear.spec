Name:           TerraGear
Version:        2018.3.2
Release:        2%{?dist}
License:        GPLv2+
Summary:        Scene Generation components
URL:            http://terragear.sourceforge.net
Source0:        https://git.code.sf.net/p/flightgear/terragear
BuildRequires:  libtiff-devel

%description
TerraGear is a collection of tools for building scenery for the
FlightGear project.

%package devel
Summary: Development libraries and headers for TerraGear
Requires: %{name} = %{version}-%{release}

%description devel
Development headers and libraries for building applications against 
TerraGear.

%prep
rm -rf terragear
git clone --single-branch --branch scenery/ws2.0 https://git.code.sf.net/p/flightgear/terragear

%build
mkdir -p terragear/build
cd terragear/build
%{cmake} .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_TESTS=OFF \
    -DSYSTEM_EXPAT=ON \
    -DBUILD_SHARED_LIBS=ON \
.
make %{?_smp_mflags} terragear

echo "#!/bin/sh" > run_tg-construct.sh
echo "cd $(dirname $0)" >> run_tg-construct.sh
echo "cd install/terragear/bin" >> run_tg-construct.sh
echo "export LD_LIBRARY_PATH=$INSTALL_DIR_SIMGEAR/lib\${LD_LIBRARY_PATH:+:}\${LD_LIBRARY_PATH}" \
       >> run_tg-construct.sh
echo "./tg-construct \$@" >> run_tg-construct.sh

echo "#!/bin/sh" > run_ogr-decode.sh
echo "cd $(dirname $0)" >> run_ogr-decode.sh
echo "cd install/terragear/bin" >> run_ogr-decode.sh
echo "export LD_LIBRARY_PATH=$INSTALL_DIR_SIMGEAR/lib\${LD_LIBRARY_PATH:+:}\${LD_LIBRARY_PATH}" \
       >> run_ogr-decode.sh
echo "./ogr-decode \$@" >> run_ogr-decode.sh

echo "#!/bin/sh" > run_genapts850.sh
echo "cd $(dirname $0)" >> run_genapts850.sh
echo "cd install/terragear/bin" >> run_genapts850.sh
echo "export LD_LIBRARY_PATH=$INSTALL_DIR_SIMGEAR/lib\${LD_LIBRARY_PATH:+:}\${LD_LIBRARY_PATH}" \
     >> run_genapts850.sh
echo "./genapts850 \$@" >> run_genapts850.sh

%install
cd terragear/build
make DESTDIR=$RPM_BUILD_ROOT install

%files
%{_bindir}/
%{_includedir}/
%{_exec_prefix}/lib/
%{_datadir}/

%changelog
* Fri Feb 01 2019 Fabrice Bellet <fabrice@bellet.info> - 2018.3.2-2
- fix for boost 1.69

* Thu Jan 31 2019 Fabrice Bellet <fabrice@bellet.info> - 2018.3.2-1
- new upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.3.1-1
- new upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.2.2-1
- new upstream release

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 2018.2.1-1
- new upstream release

* Sun Apr 08 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.1.1-1
- new upstream release

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.3.1-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.3.1-1
- new upstream release

* Thu Sep 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 2017.2.1-5
- Rebuild against OSG-3.4.1.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2017.2.1-2
- Rebuilt for Boost 1.64

* Mon May 22 2017 Tom Callaway <spot@fedoraproject.org> - 2017.2.1-1
- update to 2017.2.1

* Wed Apr 05 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.3-1
- new upstream release

* Fri Mar 03 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.2-1
- new upstream release

* Thu Feb 23 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.1-1
- new upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2016.4.4-2
- Rebuilt for Boost 1.63

* Fri Jan 06 2017 Fabrice Bellet <fabrice@bellet.info> - 2016.4.4-1
- new upstream release

* Tue Dec 06 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.3-1
- new upstream release

* Fri Nov 25 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.2-1
- new upstream release

* Mon Nov 21 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.1-1
- new upstream release

* Wed Sep 14 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-2
- new upstream release

* Thu May 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.2.1-2
- add missing BR libcurl-devel

* Thu May 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.2.1-1
- new upstream release

* Mon May  9 2016 Tom Callaway <spot@fedoraproject.org> - 2016.1.2-1
- update to 2016.1.2

* Fri Feb 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.1.1-1
- new upstream release

* Sun Feb 14 2016 Fabrice Bellet <fabrice@bellet.info> - 3.7.0-5
- math: 'void getMaxSubdiv' does not make any sense

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 3.7.0-3
- Rebuilt for Boost 1.60

* Fri Sep 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.7.0-2
- Rebuild against OSG-3.4.0.

* Thu Sep 10 2015 Tom Callaway <spot@fedoraproject.org> - 3.7.0-1
- update to 3.7.0

* Thu Sep 10 2015 Tom Callaway <spot@fedoraproject.org> - 3.6.0-1
- update to 3.6.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.4.0-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.4.0-4
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-2
- Rebuild for Gcc-5.0.1 (FTBFS, RHBZ#1212686).
- Modernize spec.
- Add %%license.

* Wed Mar 11 2015 Fabrice Bellet <fabrice@bellet.info> - 3.4.0-1
- new upstream release
- drop the JPEG_FACTORY build option

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 3.2.0-6
- rebuild (gcc5)

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 3.2.0-5
- Rebuild for boost 1.57.0

* Fri Dec 26 2014 Fabrice Bellet <fabrice@bellet.info> - 3.2.0-4
- revert "GroundLightManager: don't use smart pointers in ReferencedSingleton"

* Mon Nov 03 2014 Fabrice Bellet <fabrice@bellet.info> - 3.2.0-3
- GroundLightManager: don't use smart pointers in ReferencedSingleton

* Mon Nov 03 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.0-2
- Rebuild for RHBZ #1158669.

* Fri Oct 17 2014 Fabrice Bellet <fabrice@bellet.info> - 3.2.0-1
- new upstream release

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.0-5
- Minor patch to build on aarch64

* Thu Jul 10 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.0-4
- Rebuild against OSG-3.2.1.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 3.0.0-2
- Rebuild for boost 1.55.0

* Fri Feb 21 2014 Fabrice Bellet <fabrice@bellet.info> - 3.0.0-1
- new upstream release

* Sun Sep 22 2013 Fabrice Bellet <fabrice@bellet.info> - 2.12.0-1
- new upstream release

* Thu Aug 15 2013 Ralf Corsépius <corsepiu@fedoraproject.org> 2.10.0-4
- Rebuild against OSG-3.2.0.
- Add 0005-SimGear-2.10.0-OSG-3.2.0.patch.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.10.0-2
- Rebuild for boost 1.54.0

* Mon Feb 18 2013 Fabrice Bellet <fabrice@bellet.info> - 2.10.0-1
- new upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.8.0-3
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.8.0-2
- rebuild against new libjpeg

* Tue Sep 11 2012 Fabrice Bellet <fabrice@bellet.info> 2.8.0-1
- new upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Tom Callaway <spot@fedoraproject.org> 2.6.0-2
- check to be sure that %%n is not being set as format type (CVE-2012-2090)

* Tue Feb 28 2012 Fabrice Bellet <fabrice@bellet.info> 2.6.0-1
- new upstream release

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Tom Callaway <spot@fedoraproject.org> - 2.4.0-3
- fix boost compile issue in rawhide
- fix gcc 4.7 compile issue in rawhide

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 05 2011 Fabrice Bellet <fabrice@bellet.info> 2.4.0-1
- new upstream release

* Tue Jun 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 2.0.0-6
- Rebuild against OSG-2.8.5.

* Wed Apr 20 2011 Tom Callaway <spot@fedoraproject.org> 2.0.0-5
- nuke old bundled copy of expat, use system expat (resolves 691934)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 02 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 2.0.0-3
- Rebuild against OSG-2.8.3.

* Fri Jun 18 2010 Dan Horák <dan[at]danny.cz> 2.0.0-2
- include s390/s390x in the more-arches patch

* Fri Feb 26 2010 Fabrice Bellet <fabrice@bellet.info> 2.0.0-1
- New upstream release

* Sun Feb 14 2010 Fabrice Bellet <fabrice@bellet.info> 1.9.1-10
- Fix FTBFS (bz#564682)

* Sun Nov 29 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-9
- Fix osgParticle dependency (bz#542132)

* Sun Aug 16 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-8
- Switch to openal-soft

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 14 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-6
- Fix header file installed twice

* Mon May 11 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-5
- Rebuilt to fix bz#498584

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Hans de Goede <hdegoede@redhat.com> 1.9.1-3
- Remove rpath on x86_64

* Sun Feb 15 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-2
- Rebuild for newer OSG
- gcc44 compilation fix

* Tue Feb 03 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-1
- New upstream release

* Tue Jan 06 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.0-1
- New upstream release

* Wed Sep 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.0-5
- fix SimGear-0.3.10-notabbed_value_test.patch to apply without fuzz

* Tue May 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-4
- Rebuild for new plib

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.0-3
- Autorebuild for GCC 4.3

* Mon Jan  7 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-2
- Fix timestamp.hxx to not require the (not installed) simgear_config.h header

* Sun Jan  6 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-1
- Update to new upstream release 1.0.0
- Port various patches to 1.0.0

* Wed Oct 03 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-0.2.pre1.2
- enable alpha (bz 303161)

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-0.2.pre1.1
- rebuild for ppc32

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.11-0.3.pre1
- Update License tag for new Licensing Guidelines compliance

* Wed Jun 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-0.2.pre1
- fix ppc defines in conditional to be more complete

* Wed Jun 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-0.1.pre1
- bump to 0.3.11-0.1.pre1
- fix BZ 245320

* Fri Mar 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.10-4
- link with -release %%{version} libtool flag instead of -version, so that we
  get unique soname's for each upstream release. (Upstream gives 0 ABI
  guarantees)
- fix many undefined-non-weak-symbol's, some still remain though, see bz 208678
- work around the "thesky" bug, see bz 208678

* Wed Oct 18 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.10-3
- patch out the config internal header calls (not packaged)
- use generic libGL-devel Requires

* Tue Oct  3 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.10-2
- patch in some shared libraries

* Fri Sep 29 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.10-1
- bump to 0.3.10, fix BuildRequires

* Wed Sep  7 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.8-1
- initial package for Fedora Extras
