%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Summary:	Simple, easy-to-use paint program
Name:		gpaint-2
Version:	0.3.4
Release:	1
License:	GPLv2+
Group:		Graphics
Source0:	https://alpha.gnu.org/gnu/gpaint/gpaint-2-%{version}.tar.gz
Url:		https://www.gnu.org/software/gpaint/

BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  intltool

%description
GNU Paint. A simple, easy-to-use paint program for GNOME. This is a port of
xpaint that takes advantages of features unique to the GNOME environment.

%files -f %{name}.lang
%doc AUTHORS COPYING  NEWS README THANKS
%{_bindir}/%{name}
%{_datadir}/gpaint/glade/gpaint.glade
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}

#mdk menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Gpaint
Comment=Paint program
Exec=%{_bindir}/%{name}
Icon=graphics_section
Terminal=false
Type=Application
Categories=Graphics;
MimeType=image/gif;image/jpeg;image/png;image/bmp;image/x-eps;image/x-ico;image/x-portable-bitmap;image/x-portable-pixmap;image/x-xbitmap;image/x-xpixmap;
EOF

