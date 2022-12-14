from __future__ import unicode_literals
import os, uuid, webbrowser
from moviepy.editor import *
#import moviepy.editor as mp
from pathlib import Path
from pytube import YouTube
from transliterate import translit

f = open('vars/created.txt', 'r')
created = f.read()
f.close()

if int(created) == 0:
	name = input('Enter mod name: ')
	f = open('vars/created.txt', 'w')
	f.write('1')
	f.close()

	f = open('vars/name.txt', 'w')
	f.write(name)
	f.close()

	os.rename('None', name)

f = open('vars/MasterBundle.txt', 'r')
masterbundle = f.read()
f.close()

f = open('vars/name.txt', 'r')
name = f.read()
f.close()

f = open('vars/quality.txt', 'r')
quality = f.read()
f.close()

f = open('vars/Is_Loop.txt', 'r')
is_loop = f.read()
f.close()

request_for_command = True
while request_for_command == True:
	command = input('0. Exit the program\n1. Add song\n2. Clear masterbundle (if you need to update mod)\n3. Open URL on the Discord server of our server\nWrite the action number: ')
	if command == '1':

		test = uuid.uuid4().hex

		color = input('Color: ')

		url = input('YouTube-link (https://www.youtube.com/watch?v=...): ')

		link = url
		yt = YouTube(link)
		stream = yt.streams.filter(file_extension="mp4")
		stream[0].download()

		song_name = yt.title
		#print(test)

		#text2 = input('Name: ')
		text2 = translit(yt.title, 'ru', reversed=True)
		print(text2)

		text3 = yt.title.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '').replace('.', '').replace(',','').replace('#', '')

		text = text2.replace(' ', '').replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '').replace('.', '').replace(',','').replace('#', '')
		video = VideoFileClip(f"{text3}.mp4")
		video.audio.write_audiofile(f"{text}.mp3")
		video.close()
		#os.rename(f'{text3}.mp4', f'{text}.mp3')
		#os.rename(f'{text}.mp4', f'{text}.mp3')

		#print(text)

		path = 'Mod/Boombox/Music/'+text+'/'

		#print(path)

		os.mkdir(path)

		f = open(path+'English.dat', 'w')

		f.write(f'Name <color={color}>{text2}</color>')
		f.close()

		f = open(path+text+'.asset', 'w')
		code = """"Metadata"
		{{
			"GUID" "{test}"
			"Type" "SDG.Unturned.StereoSongAsset, Assembly-CSharp, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null"
		}}
		"Asset"
		{{
			"Song"
			{{
				"MasterBundle" "{masterbundle}.masterbundle"
				"AssetPath" "Music/{text}/{text}.mp3"
			}}
			"Is_Loop" "{is_loop}"	
		}}
		""".format(masterbundle=masterbundle, test=test, text=text, is_loop=is_loop)
		f.write(code)
		f.close()

		os.mkdir(f"{name}/Assets/Boombox/Music/{text}/")

		os.replace(f"{text}.mp3", f"{name}/Assets/Boombox/Music/{text}/{text}.mp3")

		path_to_file = f"{name}/Assets/Boombox.meta"
		path = Path(path_to_file)

		if path.is_file():
		    os.remove(path_to_file)

		new_test = uuid.uuid4().hex
		code = """fileFormatVersion: 2
guid: {new_test}
folderAsset: yes
DefaultImporter:
  externalObjects: {{}}
  userData: 
  assetBundleName: 
  assetBundleVariant: 
""".format(new_test=new_test)
		
		f = open(path_to_file, 'w')
		f.write(code)
		f.close()

		#NEW

		path_to_file = f"{name}/Assets/Editor.meta"
		path = Path(path_to_file)
		
		if path.is_file():
		    os.remove(path_to_file)

		new_test = uuid.uuid4().hex
		code = """fileFormatVersion: 2
guid: {new_test}
folderAsset: yes
DefaultImporter:
  externalObjects: {{}}
  userData: 
  assetBundleName: 
  assetBundleVariant: 
""".format(new_test=new_test)

		f = open(path_to_file, 'w')
		f.write(code)
		f.close()

		#NEW

		path_to_file = f"{name}/Assets/Scenes.meta"
		path = Path(path_to_file)
		
		if path.is_file():
		    os.remove(path_to_file)

		new_test = uuid.uuid4().hex
		code = """fileFormatVersion: 2
guid: {new_test}
folderAsset: yes
DefaultImporter:
  externalObjects: {{}}
  userData: 
  assetBundleName: 
  assetBundleVariant: 
""".format(new_test=new_test)

		f = open(path_to_file, 'w')
		f.write(code)
		f.close()
		
		#NEW

		path_to_file = f"{name}/Assets/Runtime.meta"
		path = Path(path_to_file)
		
		if path.is_file():
		    os.remove(path_to_file)

		new_test = uuid.uuid4().hex
		code = """fileFormatVersion: 2
guid: {new_test}
folderAsset: yes
DefaultImporter:
  externalObjects: {{}}
  userData: 
  assetBundleName: 
  assetBundleVariant: 
""".format(new_test=new_test)
		
		f = open(path_to_file, 'w')
		f.write(code)
		f.close()

		path_to_file = f"{name}/Assets/Boombox/Music.meta"
		path = Path(path_to_file)

		if path.is_file():
		    os.remove(path_to_file)

		new_test = uuid.uuid4().hex
		code = """fileFormatVersion: 2
guid: {new_test}
folderAsset: yes
DefaultImporter:
  externalObjects: {{}}
  userData: 
  assetBundleName: {masterbundle}.masterbundle
  assetBundleVariant: 
""".format(new_test=new_test, masterbundle=masterbundle)
		
		f = open(path_to_file, 'w')
		f.write(code)
		f.close()

		new_test = uuid.uuid4().hex
		code = """fileFormatVersion: 2
guid: {new_test}
folderAsset: yes
DefaultImporter:
  externalObjects: {{}}
  userData: 
  assetBundleName: {masterbundle}.masterbundle
  assetBundleVariant: 
""".format(new_test=new_test, masterbundle=masterbundle)

		f = open(f"{name}/Assets/Boombox/Music/{text}.meta", 'w')
		f.write(code)
		f.close()

		new_test = uuid.uuid4().hex
		code = """fileFormatVersion: 2
guid: {new_test}
AudioImporter:
  externalObjects: {{}}
  serializedVersion: 6
  defaultSettings:
    loadType: 0
    sampleRateSetting: 0
    sampleRateOverride: 44100
    compressionFormat: 1
    quality: {quality}
    conversionMode: 0
  platformSettingOverrides: {{}}
  forceToMono: 1
  normalize: 1
  preloadAudioData: 1
  loadInBackground: 0
  ambisonic: 0
  3D: 1
  userData: 
  assetBundleName: 
  assetBundleVariant: 
""".format(new_test=new_test, quality=quality)

		f = open(f"{name}/Assets/Boombox/Music/{text}/{text}.mp3.meta", 'w')
		f.write(code)
		f.close()

		os.remove(f"{text3}.mp4")

		print(f'Succesfully added song "{text2}"!\n')

	elif command == '2':
		f = open(f'Mod/Boombox/{masterbundle}.masterbundle.manifest', 'w')
		f.write('')
		f.close()
		os.remove(f'Mod/Boombox/{masterbundle}.masterbundle')

		print('Masterbundle "'+masterbundle+'" succesfully cleared!\n')
	elif command == '0':
		raise SystemExit
	elif command == '3':
		webbrowser.open('https://discord.gg/radFYMXSfK', new=2)
		print('')
	else:
		print('')