(h2 "DESCRIPTION")

(p "DNT is a Development (Note) Tracker with a command line user interface. "
   "It is somewhat similar to "
   (a (@ (href "http://swapoff.org/DevTodo")) "devtodo")
   " with a plugin-oriented design.")
(p "It aims to ease the small/medium projects management tasks (bugs "
   "tracking, feature requests, notes etc) by keeping all the required "
   "information together in the same project's source repository. ")
(p "Being a command line oriented utility it has, as a side-effect, the "
   "ability to automatize the generation of BUGS, NEWS, TODOs etc. files.")

(h2 "INSTALLATION")

(h3 "Prerequisites")
(p "In order to install DNT into your system you will need:"
(ul
 (li (a (@ (href "http://www.python.org")) "Python > 2.5") )
 )
)

(h3 "Installation")
(p "The following notes do not override your system's package management "
   "software, please follow your system's guidelines to install the software.")

(p "DNT uses the autotools facilities, the simplest way to install "
   "the package in your system is:")
(ul
 (li (kbd "cd") " to the directory containing the package's source code "
     "and type " (kbd "./configure") " to configure the package for your "
     "system."
     "Running " (kbd "configure") " might take a while. While running, "
     "it prints some messages telling which features it is checking for")
 (li "Type " (kbd "make") " to compile the package")
 (li "Optionally, type " (kbd "make check") " to run all self-tests that "
     "come with the package")
 (li "Type " (kbd "make install") " to install the programs and any data "
     "files and documentation"))

(p "Use " (kbd "./configure --help") " to get a brief help of all "
   "configuration tweaks available.")
(p "You can remove the program binaries and object files from the "
   "source code directory by typing " (kbd "make clean") ". "
   "To also remove the files that " (samp "configure") " created (so you "
   "can compile the package for a different architecture), type "
   (kbd "make distclean") ".")
(p "You can also type " (kbd "make uninstall") " to remove the installed "
   "files.")
(p "Note that the " (samp "--prefix") " option allows installation using "
   "different paths than the default ones, this option enables sandbox "
   "installations.")

(h2 "COPYING")
(p "The project is licensed under the "
   (a (@ (href "http://www.gnu.org/licenses/licenses.html"))
      "GNU General Public License, version 2"))

(h2 "MAINTAINERS")
(p "Francesco Salvestrini <salvestrini AT gmail DOT com>")

(h2 "AUTHORS")
(p "Francesco Salvestrini <salvestrini AT gmail DOT com>")

(h2 "RELEASES")
(p "Sorry, no public release available at the moment.")

(h2 "MAILING LISTS")
(p "The project has a single moderated mailing list, with an archive. "
   "In order to post a message to the mailing list you must be subscribed. "
   "Please consult the "
   (a (@ (href "http://lists.nongnu.org/mailman/listinfo/dnt-generic"))
      "mailing list page")
   " for more information on subscribing to the mailing list.")

(h2 "REPORT A BUG")
(p "If you think you have found a bug then please send as complete a report "
   "as possible to "
   "<dnt-generic AT nongnu DOT org>. "
   "An easy way to collect all the required information, such as platform and "
   "compiler, is to include in your report the config.log file available at "
   "the end of the configuration procedure.")
(p "If you have a patch for a bug that hasn't yet been fixed in "
   "the latest repository sources, please be so kind to create it using the "
   "repository sources, not the release sources.")

(h2 "DEVELOPMENT")

(h3 "Browsing sources")
(p "You can browse the "
   (a (@ (href "http://git.savannah.nongnu.org/gitweb/?p=dnt.git"))
      "Git repository")
   " of this project with your web browser. This gives you a good "
   "picture of the current status of the source files. You may also view "
   "the complete histories of any file in the repository as well as "
   "differences among two versions.")

(h3 "Getting a copy of the Git Repository")
(p "Anonymous checkout:")
(pre (@ class "terminal")
     (a (@ (href "http://savannah.gnu.org/maintenance/UsingGit")) "git")
     " clone git://git.savannah.nongnu.org/dnt.git")

(h3 "Contribute")
(p "If you have time and programming skills, you can help us by developing "
   "missing features, regression tests or bug-fixing the present codebase. "
   "Subscribe to the "
   (a (@ (href "http://lists.nongnu.org/mailman/listinfo/dnt-generic"))
      "mailing list")
   ", drop us a mail and start coding. Send your code to the "
   "mailing list under the form of patches for the current revision system.")
(p "If you have time but no programming skills, you can help with "
   "documentation,  packaging, tests before releases etc ...")
