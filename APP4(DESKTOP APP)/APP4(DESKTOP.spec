# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Objects\\py_real_world_app\\APP4(DESKTOP', 'APP)\\dist\\bs.ico', 'bookstore.py'],
             pathex=['C:\\Users\\jpoola\\3D Objects\\py_real_world_app\\APP4(DESKTOP APP)'],
             binaries=[],
             datas=[],
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
          name='APP4(DESKTOP',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\jpoola\\3D')