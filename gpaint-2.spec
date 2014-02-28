Summary:	Simple, easy-to-use paint program
Name:		gpaint-2
Version:	0.3.3
Release:	8
License:	GPLv2+
Group:		Graphics
Source0:	http://www.gnu.org/software/gpaint/downloading/%{name}-%{version}.tar.gz
Url:		http://www.gnu.org/software/gpaint/
Patch0:		gpaint-2-0.3.3-fix-drawing-fnt.patch
Patch1:		gpaint-2-0.3.3-remove-entry-menu.h.patch
Patch2:		gpaint-2-0.3.3-fix-crash-on-font-selection.patch
Patch3:		gpaint-2-0.3.3-fix-crash-on-saving-in-unsupported-format.patch
Patch4:		gpaint-2-0.3.3-fix-not-printable-string.patch
Patch5:		gpaint-2-0.3.3-fix-color-selection.patch
BuildRequires:	pkgconfig(libglade-2.0)

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
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%configure2_5x
%make LIBS="-lm"

%install
%makeinstall_std
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

