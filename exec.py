import libtorrent as lt
import time
import sys
import os

ses = lt.session()
ses.listen_on(6881, 6891)

print(' Modulo II (Prática) - Trabalho de Sistemas Distribuidos')
print('Gilberty A. S. Macedo')
print('201811316010')
print('')

if len(sys.argv) >= 2:
	arq = sys.argv[1]
	torrent = lt.torrent_info(arq)
	h = ses.add_torrent({'ti': torrent, 'save_path': './'})
	s = h.status()

	print('Baixando o arquivo: ', s.name)

	while (not s.is_seeding):
	    s = h.status()
	    print('\r%.2f%% - peers: %d) %s' % (s.progress * 100, s.num_peers, s.state), end=' ')

	    alerts = ses.pop_alerts()
	    for a in alerts:
		if a.category() & lt.alert.category_t.error_notification:
		    print(a)
	    sys.stdout.flush()
	    time.sleep(1)

	print(h.status().name, "Arquivo baixado com sucesso!")

	print('')
	print('Atividade realizada para fins educacionais.')
else:
	print('Você precisa digitar o nome do arquivo para fazer download!')
	print('python3 exec.py <nomedoarquivo>.torrent')
