import re

from mcdreforged.api.all import *

playerList = []
onflag = False

def on_player_joined(server: PluginServerInterface, player: str, info: Info):
	global playerList
	if server.get_permission_level(obj = player) >= 2:
		playerList.append(player)

def on_player_left(server: PluginServerInterface, player: str):
	global playerList
	try:
		playerList.remove(player)
	except:
		pass

def on_load(server, prev):
	server.logger.info('MCDR to Chat onload')

def on_info(server: PluginServerInterface, info: Info):
	global playerList
	global onflag
	if re.fullmatch('ToChatLog', info.raw_content) is None and onflag:
		for player in playerList:
			server.tell(player, f'[ToChatLog]{info.raw_content}')
	if info.player is not None and server.get_permission_level(obj = info.player) >= 2 and info.content == '!!tochat on':
		onflag = True
	if info.player is not None and server.get_permission_level(obj = info.player) >= 2 and info.content == '!!tochat off':
		onflag = False
	if info.player is not None and server.get_permission_level(obj = info.player) >= 2 and info.content == '!!tochat':
		server.tell(info.player, f'[ToChatLog]!!tochat on开启\n[ToChatLog]!!tochat off关闭')
		server.tell(info.player, f'[ToChatLog]!!tochat join参与监听\n[ToChatLog]!!tochat exit退出监听\n[ToChatLog]当前状态{onflag}')
		members = 'Members: '
		for player in playerList:
			members = members + player + ' '
		server.tell(info.player, f'[ToChatLog]{members}')
	if info.player is not None and server.get_permission_level(obj = info.player) >= 2 and info.content == '!!tochat join':
		try:
			playerList.remove(info.player)
		except:
			pass
		playerList.append(info.player)
	if info.player is not None and server.get_permission_level(obj = info.player) >= 2 and info.content == '!!tochat exit':
		try:
			playerList.remove(info.player)
		except:
			pass
