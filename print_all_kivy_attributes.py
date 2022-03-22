import re
from cprint import cprint
def print_all_widget_attributes(di, prefix='self.root.ids.'):
    if not any(list(di.keys())):
        errormessage = f'      Nothing found in: {prefix.strip(".")}      '
        errormessage_hi = len(errormessage) * '-'
        print(cprint.red(f'{errormessage_hi}\n{errormessage}\n{errormessage_hi}', False))
        return None
    for key, item in di.items():
        message = f'↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ Widget: {str(key)} ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'
        message_hi = len(message) * '-'
        print(cprint.yellow(f'{message_hi}\n{message}\n{message_hi}', False))

        try:
            for i in dir(item):
                if i !='ids':
                    print(
                        cprint.blue(prefix, False)
                        + cprint.red(key, False)
                        + cprint.yellow(".", False)
                        + cprint.green(i, False),
                        end=cprint.white("=", False),
                    )
                    exec(
                        f'if (str(item.{i}).startswith("<")): print(cprint.white(item.{i}, False))\nelif not (str(item.{i}).startswith("<")): print(cprint.yellow(item.{i}, False))'
                    )
                elif i == 'ids':
                    print_all_widget_attributes(item.ids, prefix=re.sub(r'\.+', '.', f'{prefix}.{key}.ids.'))
        except Exception as Fehler:
            print(Fehler)