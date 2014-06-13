# revision 20075
# category Package
# catalog-ctan /fonts/poltawski
# catalog-date 2010-10-12 09:30:05 +0200
# catalog-license gfsl
# catalog-version 1.101
Name:		texlive-poltawski
Version:	1.101
Release:	7
Summary:	Antykwa Poltawskiego Family of Fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/poltawski
License:	GFSL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poltawski.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poltawski.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains the Antykwa Poltawskiego family of fonts
in the PostScript Type 1 and OpenType formats. The original
font was designed in the twenties of the XX century by the
Polish typographer Adam Poltawski(1881-1952). Following the
route set out by the Latin Modern and TeX Gyre projects
(http://www.gust.org.pl/projects/e-foundry), the Antykwa
Poltawskiego digitisation project aims at providing a rich
collection of diacritical characters in the attempt to cover as
many Latin-based scripts as possible. To our knowledge, the
repertoire of characters covers all European languages as well
as some other Latin-based alphabets such as Vietnamese and
Navajo; at the request of users, recent extensions (following
the enhancement of the Latin Modern collection) provide glyphs
sufficient for typesetting of romanized transliterations of
Arabic and Sanskrit scripts. The Antykwa Poltawskiego family
consists of 4 weights (light, normal, medium, bold), each
having upright and italic forms and one of 5 design sizes: 6,
8, 10, 12 and 17pt (in the OTF lingo: extended, semiextended,
normal, semicondensed, and condensed, respectively).
Altogether, the collection comprises 40 font files, containing
the same repertoire of 1126 characters. The preliminary version
of Antykwa Poltawskiego (antp package) released in 2000 is
rendered obsolete by this package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpb10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpb12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpb17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpb6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpb8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpbi10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpbi12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpbi17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpbi6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpbi8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpl10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpl12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpl17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpl6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpl8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpli10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpli12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpli17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpli6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpli8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpm10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpm12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpm17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpm6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpm8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpmi10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpmi12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpmi17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpmi6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpmi8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpr10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpr12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpr17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpr6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpr8.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpri10.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpri12.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpri17.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpri6.afm
%{_texmfdistdir}/fonts/afm/gust/poltawski/antpri8.afm
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-cs-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-cs.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-ec-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-ec.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-l7x-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-l7x.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-qx-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-qx.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-rm-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-rm.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-t5-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-t5.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-texnansi-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-texnansi.enc
%{_texmfdistdir}/fonts/enc/dvips/poltawski/ap-ts1.enc
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-cs.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-ec.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-l7x.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-qx.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-rm.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-t5.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap-ts1.map
%{_texmfdistdir}/fonts/map/dvips/poltawski/ap.map
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpolt-bold.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpolt-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpolt-italic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpolt-regular.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltcond-bold.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltcond-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltcond-italic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltcond-regular.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltexpd-bold.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltexpd-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltexpd-italic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltexpd-regular.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltlt-bold.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltlt-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltlt-italic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltlt-regular.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltcond-bold.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltcond-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltcond-italic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltcond-regular.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltexpd-bold.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltexpd-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltexpd-italic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltexpd-regular.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemicond-bold.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemicond-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemicond-italic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemicond-regular.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemiexpd-bold.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemiexpd-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemiexpd-italic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltltsemiexpd-regular.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemicond-bold.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemicond-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemicond-italic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemicond-regular.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemiexpd-bold.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemiexpd-bolditalic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemiexpd-italic.otf
%{_texmfdistdir}/fonts/opentype/gust/poltawski/antpoltsemiexpd-regular.otf
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/cs-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ec-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/l7x-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/qx-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/rm-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/t5-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri10-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri12-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri17-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri6-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri8-sc.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/texnansi-antpri8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpb10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpb12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpb17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpb6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpb8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpbi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpbi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpbi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpbi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpbi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpl10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpl12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpl17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpl6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpl8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpli10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpli12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpli17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpli6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpli8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpm10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpm12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpm17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpm6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpm8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpmi10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpmi12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpmi17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpmi6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpmi8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpr10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpr12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpr17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpr6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpr8.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpri10.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpri12.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpri17.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpri6.tfm
%{_texmfdistdir}/fonts/tfm/gust/poltawski/ts1-antpri8.tfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb10.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb12.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb17.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb6.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpb8.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi10.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi12.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi17.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi6.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpbi8.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl10.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl12.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl17.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl6.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpl8.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli10.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli12.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli17.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli6.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpli8.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm10.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm12.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm17.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm6.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpm8.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi10.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi12.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi17.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi6.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpmi8.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr10.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr12.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr17.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr6.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpr8.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri10.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri10.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri12.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri12.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri17.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri17.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri6.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri6.pfm
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri8.pfb
%{_texmfdistdir}/fonts/type1/gust/poltawski/antpri8.pfm
%{_texmfdistdir}/tex/latex/poltawski/antpolt.sty
%{_texmfdistdir}/tex/latex/poltawski/il2antp.fd
%{_texmfdistdir}/tex/latex/poltawski/il2antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/l7xantp.fd
%{_texmfdistdir}/tex/latex/poltawski/l7xantpl.fd
%{_texmfdistdir}/tex/latex/poltawski/ly1antp.fd
%{_texmfdistdir}/tex/latex/poltawski/ly1antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/ot1antp.fd
%{_texmfdistdir}/tex/latex/poltawski/ot1antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/ot4antp.fd
%{_texmfdistdir}/tex/latex/poltawski/ot4antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/qxantp.fd
%{_texmfdistdir}/tex/latex/poltawski/qxantpl.fd
%{_texmfdistdir}/tex/latex/poltawski/t1antp.fd
%{_texmfdistdir}/tex/latex/poltawski/t1antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/t5antp.fd
%{_texmfdistdir}/tex/latex/poltawski/t5antpl.fd
%{_texmfdistdir}/tex/latex/poltawski/ts1antp.fd
%{_texmfdistdir}/tex/latex/poltawski/ts1antpl.fd
%doc %{_texmfdistdir}/doc/fonts/poltawski/GUST-FONT-LICENSE.txt
%doc %{_texmfdistdir}/doc/fonts/poltawski/MANIFEST-Antykwa-Poltawskiego.txt
%doc %{_texmfdistdir}/doc/fonts/poltawski/README-Antykwa-Poltawskiego.txt
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpb10.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpb12.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpb17.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpb6.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpb8.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpbi10.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpbi12.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpbi17.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpbi6.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpbi8.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpl10.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpl12.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpl17.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpl6.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpl8.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpli10.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpli12.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpli17.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpli6.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpli8.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpm10.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpm12.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpm17.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpm6.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpm8.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpmi10.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpmi12.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpmi17.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpmi6.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpmi8.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpr10.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpr12.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpr17.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpr6.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpr8.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpri10.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpri12.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpri17.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpri6.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/antpri8.fea
%doc %{_texmfdistdir}/doc/fonts/poltawski/ap-hist.txt
%doc %{_texmfdistdir}/doc/fonts/poltawski/ap-info.pdf
%doc %{_texmfdistdir}/doc/fonts/poltawski/ap-logo.pdf
%doc %{_texmfdistdir}/doc/fonts/poltawski/goadb100.nam
%doc %{_texmfdistdir}/doc/fonts/poltawski/tstapot1.pdf
%doc %{_texmfdistdir}/doc/fonts/poltawski/tstapot1.tex
%doc %{_texmfdistdir}/doc/fonts/poltawski/tstapot4.pdf
%doc %{_texmfdistdir}/doc/fonts/poltawski/tstapot4.tex
%doc %{_texmfdistdir}/doc/fonts/poltawski/tstapqx.pdf
%doc %{_texmfdistdir}/doc/fonts/poltawski/tstapqx.tex
%doc %{_texmfdistdir}/doc/fonts/poltawski/tstapt1.pdf
%doc %{_texmfdistdir}/doc/fonts/poltawski/tstapt1.tex
%doc %{_texmfdistdir}/doc/fonts/poltawski/tstapts1.pdf
%doc %{_texmfdistdir}/doc/fonts/poltawski/tstapts1.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.101-2
+ Revision: 755006
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.101-1
+ Revision: 719282
- texlive-poltawski
- texlive-poltawski
- texlive-poltawski
- texlive-poltawski

