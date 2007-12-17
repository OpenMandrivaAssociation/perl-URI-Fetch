%define module  URI-Fetch
%define name    perl-%{module}
%define release %mkrel 2
%define version 0.08

Name:               %{name}
Version:            %{version}
Release:            %{release}
Summary:            Perl Module for Smart URI fetching/caching
License:            GPL or Artistic
Group:              Development/Perl
Url:                http://search.cpan.org/dist/%{module}/
Source:             http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
BuildRequires:      perl(Class::ErrorHandler)
BuildRequires:      perl(LWP::UserAgent)
BuildRequires:      perl(URI)
BuildRequires:      perl(Storable)
BuildRequires:      perl(Compress::Zlib)
BuildRequires:      perl(Cache)
BuildArch:          noarch

%description
Perl Module for Smart URI fetching/caching.

%prep
%setup -q -n %{module}-%{version}

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


