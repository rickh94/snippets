from pathlib import Path
import os
import re
import sys

pattern = re.compile(r'(?<!^)(?=[A-Z])')

full_path = Path(sys.argv[1]).expanduser()
folder = full_path.name
prefix = folder.title()
output_path = Path(sys.argv[2]).expanduser()

for item in os.listdir(full_path):
    name =  item.split('.')[0]
    lines = []
    lines.append("import { mount } from '@vue/test-utils';")
    lines.append(f"import {prefix}{name} from '~/components/{folder}/{item}';")
    lines.append("")
    lines.append(f"describe('{prefix}{name}', () => " + "{")
    lines.append("  test('matches snapshot', () => {")
    lines.append(f"    const wrapper = mount({prefix}{name});")
    lines.append("    expect(wrapper).toMatchSnapshot();")
    lines.append("  });")
    lines.append("});")
    walrus_name = pattern.sub('-', name).lower()
    with open(f'{output_path}/{folder}/{walrus_name}.test.js', 'w') as fp:
        fp.write('\n'.join(lines))
    
    
