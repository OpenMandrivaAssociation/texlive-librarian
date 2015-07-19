# revision 19880
# category Package
# catalog-ctan /macros/generic/librarian
# catalog-date 2010-06-25 08:56:08 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-librarian
Version:	1.0
Release:	10
Summary:	Tools to create bibliographies in TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/librarian
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librarian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librarian.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extracts information in bib files, makes it
available in the current document, and sorts lists of entries
according to that information and the user's specifications.
Citation and bibliography styles can then be written directly
in TeX, without any use of BibTeX. Creating references thus
depends entirely on the user's skill in TeX. The package works
with all formats that use plain TeX's basic syntactic sugar;
the distribution includes a third-party file for ConTeXt and a
style file for LaTeX. As an example of use, an Author (Year)
style is given in a separate file and explained in the
documentation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/librarian/librarian.sty
%{_texmfdistdir}/tex/generic/librarian/librarian.tex
%{_texmfdistdir}/tex/generic/librarian/t-librarian.tex
%doc %{_texmfdistdir}/doc/generic/librarian/README
%doc %{_texmfdistdir}/doc/generic/librarian/authoryear.tex
%doc %{_texmfdistdir}/doc/generic/librarian/librarian-doc.pdf
%doc %{_texmfdistdir}/doc/generic/librarian/librarian-doc.tex
%doc %{_texmfdistdir}/doc/generic/librarian/librarian.bib

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 753307
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718857
- texlive-librarian
- texlive-librarian
- texlive-librarian
- texlive-librarian

