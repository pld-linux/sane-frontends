%define	gimp_ver	1.1
Summary:	SANE --- Easy local and networked scanner access
Summary(pl):	SANE --- Prosta obs³uga skanerów lokalnych i sieciowych
Name:		sane-frontends
Version:	1.0.4
Release:	1
Group:		Libraries
Group(pl):	Biblioteki
License:	GPL
Source0:	ftp://ftp.mostang.com/pub/sane/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.mostang.com/sane/
BuildRequires:	sane-backends-devel
BuildRequires:	gimp-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6
%define _mandir	/usr/X11R6/man

%description
SANE (Scanner Access Now Easy) is a sane and simple interface to both
local and networked scanners and other image acquisition devices like
digital still and video cameras. SANE currently includes modules for
accessing:

Scanners: Agfa SnapScan, Apple, Artec, Canon, CoolScan, Epson, HP,
          Microtek, Mustek, Nikon, Siemens, Tamarack, UMAX

Others:   Connectix, QuickCams

and other SANE devices via network.

This packages contains various frontends for SANE.

%description -l pl
SANE (Scanner Access Now Easy) jest rozs±dnym i prostym insterfejsem
do skanerów, zarówno lokalnych jak i sieciowych, oraz innych urz±dzeñ
do pozyskiwania obrazów, jak cyfrowe aparaty i kamery. SANE aktualnie
zawiera modu³y do obs³ugi:

Skanery: Agfa SnapScan, Apple, Artec, Canon, CoolScan, Epson, HP,
         Microtek, Mustek, Nikon, Siemens, Tamarack, UMAX

Inne:    Connectix, QuickCams

oraz inne urz±dzenia dostêpne przez sieæ.

Ten pakiet zawiera ró¿ne frontendy dla SANE.

%prep
%setup -q
%patch0 -p1

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/gimp/%{gimp_ver}/plug-ins
ln -sf %{_bindir}/xscanimage $RPM_BUILD_ROOT%{_libdir}/gimp/%{gimp_ver}/plug-ins

gzip -9nf AUTHORS NEWS PROBLEMS TODO Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/gimp/%{gimp_ver}/plug-ins/*
%{_mandir}/man1/*
%{_datadir}/*
