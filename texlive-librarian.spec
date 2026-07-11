%global tl_name librarian
%global tl_revision 19880

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Tools to create bibliographies in TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/librarian
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/librarian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/librarian.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extracts information in bib files, makes it available in the
current document, and sorts lists of entries according to that
information and the user's specifications. Citation and bibliography
styles can then be written directly in TeX, without any use of BibTeX.
Creating references thus depends entirely on the user's skill in TeX.
The package works with all formats that use plain TeX's basic syntactic
sugar; the distribution includes a third-party file for ConTeXt and a
style file for LaTeX. As an example of use, an Author (Year) style is
given in a separate file and explained in the documentation.

