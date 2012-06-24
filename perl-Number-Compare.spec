%include	/usr/lib/rpm/macros.perl
%define	pdir	Number
%define	pnam	Compare
Summary:	Number::Compare - numeric comparisons
Summary(pl):	Number::Compare - por�wnywanie liczb
Name:		perl-Number-Compare
Version:	0.01
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	519a4434e35033e9bd034d27cd2fd299
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Number::Compare compiles a simple comparison to an anonymous
subroutine, which you can call with a value to be tested again.

%description -l pl
Number::Compare kompiluje proste por�wnanie do anonimowej biblioteki,
kt�r� mo�na wywo�a� ponownie dla por�wnywanej warto�ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Number/Compare.pm
%{_mandir}/man3/*
