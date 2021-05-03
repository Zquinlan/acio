# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['acio_gui.py'],
             binaries=[],
             datas=[('theme_images/Alembic.png', '.'), ('theme_images/Bulma.png', '.'), ('theme_images/Minimal.png', '.'), ('Acio_design_v0.01.png', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='acio_gui',
          icon='Acio_design_v0.01.png',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , 
          manifest='')
