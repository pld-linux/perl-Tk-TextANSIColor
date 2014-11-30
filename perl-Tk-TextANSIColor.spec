#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working $DISPLAY)

%define		pdir	Tk
%define		pnam	TextANSIColor
%include	/usr/lib/rpm/macros.perl
Summary:	Tk::TextANSIColor - Tk::Text widget with support for ANSI color escape codes
Summary(pl.UTF-8):	Tk::TextANSIColor - widget Tk::Text z obsługą sekwencji kolorów ANSI
Name:		perl-Tk-TextANSIColor
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c285af9d6189baab4c8a9cc22dcc3ad0
URL:		http://search.cpan.org/dist/Tk-TextANSIColor/
BuildRequires:	perl-Term-ANSIColor >= 1.00
BuildRequires:	perl-Tk
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Term-ANSIColor >= 1.00
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This widget extends the capabilities of the standard Tk::Text widget
by adding support for ANSI color escape codes. When these escape codes
are detected they are replaced by equivalent tags. A read-only widget
is also supplied.

%description -l pl.UTF-8
Ten widget rozszerza możliwości standardowego widgetu Tk::Text dodając
obsługę kodów kolorów ANSI. Jeśli te kody zostaną wykryte, są
zastępowane odpowiednimi znacznikami. Załączony jest także widget
tylko do odczytu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT

./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Tk/*TextANSIColor.pm
%{_mandir}/man3/*
