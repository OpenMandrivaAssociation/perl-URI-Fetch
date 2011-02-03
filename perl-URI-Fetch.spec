%define upstream_name    URI-Fetch
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl Module for Smart URI fetching/caching
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: perl(Class::ErrorHandler)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(URI)
BuildRequires: perl(Storable)
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(Cache)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Perl Module for Smart URI fetching/caching.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
SKIP_SAX_INSTALL=1 CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/URI
%{_mandir}/*/*
