def parse_groups(lines):
  groups = []
  group = []
  for line in lines:
    if line != '':
      group.append(line)
    else:
      groups.append(group)
      group = []
  groups.append(group)
  return groups
