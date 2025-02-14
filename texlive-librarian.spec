Name:		texlive-librarian
Version:	19880
Release:	2
Summary:	Tools to create bibliographies in TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/librarian
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librarian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/librarian.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
