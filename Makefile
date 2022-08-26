publish:
	python3 fix_tags.py
	scp blog/*.md prose.sh:/

