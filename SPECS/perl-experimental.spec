Name:           perl-experimental
Version:        0.022
Release:        6%{?dist}
Summary:        Experimental features made easy
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/experimental
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/experimental-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# feature is highly recommended on perl >= 5.10
BuildRequires:  perl(feature)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(Test::More) >= 0.89
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
# feature is highly recommended on perl >= 5.10
Requires:       perl(feature)

%description
This pragma provides an easy and convenient way to enable or disable
experimental features.

%prep
%setup -q -n experimental-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.022-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.022-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.022-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.022-2
- Perl 5.32 rebuild

* Tue May 05 2020 Petr Pisar <ppisar@redhat.com> - 0.022-1
- 0.022 bump

* Mon Feb 24 2020 Petr Pisar <ppisar@redhat.com> - 0.021-1
- 0.021 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-439
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.020-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.020-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.020-2
- Perl 5.28 rebuild

* Thu May 10 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.020-1
- 0.020 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Petr Pisar <ppisar@redhat.com> - 0.019-1
- 0.019 bump

* Fri Dec 01 2017 Petr Pisar <ppisar@redhat.com> - 0.018-1
- 0.018 bump

* Wed Nov 15 2017 Petr Pisar <ppisar@redhat.com> - 0.017-1
- 0.017 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.016-394
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.016-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.016-366
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.016-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.016-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Petr Pisar <ppisar@redhat.com> - 0.016-1
- 0.016 bump

* Mon Oct 05 2015 Petr Pisar <ppisar@redhat.com> - 0.015-1
- 0.015 bump

* Mon Sep 14 2015 Petr Pisar <ppisar@redhat.com> - 0.014-1
- 0.014 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.013-346
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.013-3
- Perl 5.22 rebuild

* Thu Dec 11 2014 Petr Pisar <ppisar@redhat.com> - 0.013-2
- Use ExtUtils::MakeMaker for building

* Mon Oct 27 2014 Petr Pisar <ppisar@redhat.com> - 0.013-1
- 0.013 bump

* Mon Oct 13 2014 Petr Pisar <ppisar@redhat.com> - 0.012-1
- 0.012 bump

* Mon Sep 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.011-1
- 0.011 bump

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.010-2
- Perl 5.20 rebuild

* Fri Aug 22 2014 Petr Pisar <ppisar@redhat.com> - 0.010-1
- 0.010 bump

* Mon Aug 18 2014 Petr Pisar <ppisar@redhat.com> - 0.009-1
- 0.009 bump

* Mon Jul 07 2014 Petr Pisar <ppisar@redhat.com> - 0.008-1
- 0.008 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 14 2014 Petr Pisar <ppisar@redhat.com> - 0.007-1
- 0.007 bump

* Mon Jan 20 2014 Petr Pisar <ppisar@redhat.com> - 0.006-1
- 0.006 bump

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.005-2
- Perl 5.18 rebuild

* Mon Jun 10 2013 Petr Pisar <ppisar@redhat.com> - 0.005-1
- 0.005 bump

* Fri Jun 07 2013 Petr Pisar <ppisar@redhat.com> - 0.004-1
- 0.004 bump

* Wed May 29 2013 Petr Pisar <ppisar@redhat.com> 0.003-1
- Specfile autogenerated by cpanspec 1.78.
