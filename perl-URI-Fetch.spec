%define upstream_name    URI-Fetch
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Perl Module for Smart URI fetching/caching
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(Class::ErrorHandler)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(URI)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(Cache)
BuildArch:	noarch

%description
Perl Module for Smart URI fetching/caching.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
SKIP_SAX_INSTALL=1 CFLAGS="%{optflags}" perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/URI
%{_mandir}/*/*

%changelog
* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 635557
- update to new version 0.09

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 401931
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.08-5mdv2009.0
+ Revision: 258727
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.08-4mdv2009.0
+ Revision: 246675
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.08-2mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-2mdv2007.0
+ Revision: 133516

* Fri Mar 02 2007 Shlomi Fish  0.08-2mdv2007.1
- Fixed to noarch.
- Fixed Requires to BuildRequires

* Thu Mar 01 2007 Shlomi Fish  0.08-1mdv2007.1
- Initial release. Adapted the Feed-Find spec for this one.

