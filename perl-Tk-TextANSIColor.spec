#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working $DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	TextANSIColor
Summary:	Tk::TextANSIColor - Tk::Text widget with support for ANSI color escape codes
Summary(pl):	Tk::TextANSIColor - widget Tk::Text z obs³ug± sekwencji kolorów ANSI
Name:		perl-Tk-TextANSIColor
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	594d7c3facf2d88b9a9b075935534521
BuildRequires:	perl-Term-ANSIColor >= 1.00
BuildRequires:	perl-Tk
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Term-ANSIColor >= 1.00
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This widget extends the capabilities of the standard Tk::Text widget
by adding support for ANSI color escape codes. When these escape
codes are detected they are replaced by equivalent tags. A read-only
widget is also supplied.

%description -l pl
Ten widget rozszerza mo¿liwo¶ci standardowego widgetu Tk::Text dodaj±c
obs³ugê kodów kolorów ANSI. Je¶li te kody zostan± wykryte, s±
zastêpowane odpowiednimi znacznikami. Za³±czony jest tak¿e widget
tylko do odczytu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Tk/*TextANSIColor.pm
%{_mandir}/man3/*
