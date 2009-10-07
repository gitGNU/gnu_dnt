autogen definitions sitetool;

common = {
	layout = "./layout.sxml";
};

vars = {
        sitename          = "DNT";
        package_url       = "http://www.nongnu.org/dnt";
        package_bugreport = "dnt-generic@nongnu.org";
        ohloh_badge_url   = "http://www.ohloh.net/p/286819/widgets/project_partner_badge.js";
};

include "contents.as"
include "pages.as"
include "map.as"
include "files.as"
