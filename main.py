from snowboy import snowboydecoder


def lightsOn():
	print('Lights are on')
	detector.start(hugo)

def hugo():
	print('Success')
	detector = snowboydecoder.HotwordDetector('LightsOn.pmdl',sensitivity = 0.6, audio_gain = 1)
	detector.start(lightsOn)







print('Listening...')


detector = snowboydecoder.HotwordDetector('ok_hugo.pmdl',sensitivity = 0.6, audio_gain = 1)
detector.start(hugo)
detector.terminate()
