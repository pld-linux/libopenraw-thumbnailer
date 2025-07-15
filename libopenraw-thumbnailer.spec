Summary:	RawThumbnailer - RAW files thumbnailer for the GNOME Nautilus file manager
Summary(pl.UTF-8):	RawThumbnailer - program do miniaturek plików RAW dla zarządcy plików Nautilus
Name:		libopenraw-thumbnailer
Version:	47.0.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	https://download.gnome.org/sources/raw-thumbnailer/47/raw-thumbnailer-%{version}.tar.xz
# Source0-md5:	b0ba26935f01b916b2f8875a7ce00ab0
URL:		https://libopenraw.freedesktop.org/raw-thumbnailer/
BuildRequires:	cargo
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	rust
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	shared-mime-info
Obsoletes:	raw-thumbnailer < 0.99
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RawThumbnailer is a thumbnailer for RAW files that works with the
GNOME Nautilus file manager.

%description -l pl.UTF-8
RawThumbnailer to program generujący miniaturki plików RAW działający
z zarządcą plików Nautilus ze środowiska GNOME.

%prep
%setup -q -n raw-thumbnailer-%{version}

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database

%postun
%update_mime_database

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README
%attr(755,root,root) %{_bindir}/raw-thumbnailer
%{_datadir}/mime/packages/raw-thumbnailer.xml
%{_datadir}/thumbnailers/raw.thumbnailer
