#!/usr/bin/python

def kdeglobals(config, user):
    kdeglobals_config = [
        """[KFileDialog Settings]""",
        """Allow Expansion=false""",
        """Automatically select filename extension=true""",
        """Breadcrumb Navigation=true""",
        """Decoration position=2""",
        """LocationCombo Completionmode=5""",
        """PathCombo Completionmode=5""",
        """Show Bookmarks=false""",
        """Show Full Path=false""",
        """Show Inline Previews=true""",
        """Show Preview=false""",
        """Show Speedbar=true""",
        """Show hidden files=true""",
        """Sort by=Name""",
        """Sort directories first=true""",
        """Sort hidden files last=false""",
        """Sort reversed=false""",
        """Speedbar Width=147""",
        """View Style=DetailTree""",
        """[General]""",
        """TerminalApplication=kitty""",
        """[Icons]""",
        f"""Theme={config["icon-theme"]}"""
    ]

    with open(f"/home/{user}/.config/kdeglobals", "w", encoding="UTF-8") as file:
        file.writelines("\n".join(kdeglobals_config))