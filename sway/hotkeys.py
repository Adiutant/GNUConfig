import re

regex = r'bindsym (\$[\w\+]+) ([\w \$]+)'

regex_mod = r'set \$mod (\w+)'
config = open("config", 'r')
data = config.read()
mod = re.finditer(regex_mod, data, re.MULTILINE)
matches = re.finditer(regex, data, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
          "HOTKEY {hotkey_group} ||| FUNC {func_group}\n"
          "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n".format(hotkey_group=match.group(1),
                                                                            func_group=match.group(2)))

for _, match_mod in enumerate(mod, start=1):
    print("MOD KEY IS LIKELY {mod_key}".format(mod_key=match_mod.group(1)))
