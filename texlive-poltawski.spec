%global tl_name poltawski
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.101
Release:	%{tl_revision}.1
Summary:	Antykwa Poltawskiego Family of Fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/poltawski
License:	gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poltawski.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poltawski.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains the Antykwa Poltawskiego family of fonts in the
PostScript Type 1 and OpenType formats. The original font was designed
in the twenties of the XX century by the Polish typographer Adam
Poltawski(1881-1952). Following the route set out by the Latin Modern
and TeX Gyre projects (https://www.gust.org.pl/projects/e-foundry), the
Antykwa Poltawskiego digitisation project aims at providing a rich
collection of diacritical characters in the attempt to cover as many
Latin-based scripts as possible. To our knowledge, the repertoire of
characters covers all European languages as well as some other Latin-
based alphabets such as Vietnamese and Navajo; at the request of users,
recent extensions (following the enhancement of the Latin Modern
collection) provide glyphs sufficient for typesetting of romanized
transliterations of Arabic and Sanskrit scripts. The Antykwa
Poltawskiego family consists of 4 weights (light, normal, medium, bold),
each having upright and italic forms and one of 5 design sizes: 6, 8,
10, 12 and 17pt. Altogether, the collection comprises 40 font files,
containing the same repertoire of 1126 characters. The preliminary
version of Antykwa Poltawskiego (antp package) released in 2000 is
rendered obsolete by this package.

