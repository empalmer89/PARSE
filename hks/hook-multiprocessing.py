from PyInstaller.utils.hooks import collect_submodules, collect_data_files, exec_statement, collect_all


datas, binaries, hiddenimports = collect_all('multiprocessing', include_py_files=True)

print("\n\nDATAS (multiprocessing): ")
print(len(datas))


print("\n\nBINARIES (multiprocessing): ")
print(len(binaries))

print("\n\nHIDDENIMPORTS (multiprocessing): ")
print(len(hiddenimports))

print("\n\n")

# https://stackoverflow.com/questions/49085970/no-such-file-or-directory-error-using-pyinstaller-and-scrapy/49092020#49092020
