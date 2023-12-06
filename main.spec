# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\fellinhell\\Desktop\\GitHub\\appforstaff\\app_db.db', '.'), ('C:\\Users\\fellinhell\\Desktop\\GitHub\\appforstaff\\Fonts\\*', 'Fonts'), ('C:\\Users\\fellinhell\\Desktop\\GitHub\\appforstaff\\apple-icon-152x152.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\fellinhell\\Desktop\\GitHub\\appforstaff\\icon-152x152.ico'],
)
