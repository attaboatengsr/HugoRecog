from snowboy import snowboydecoder


def foo():
	print('something')
	detector.start(hugo)

def hugo():
	print('success')
	detector = snowboydecoder.HotwordDetector('wow.pmdl',sensitivity = 0.6, audio_gain = 1)
	detector.start(foo)










detector = snowboydecoder.HotwordDetector('ok_hugo.pmdl',sensitivity = 0.6, audio_gain = 1)
detector.start(hugo)
detector.terminate()
