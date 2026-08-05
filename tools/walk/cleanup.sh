#!/bin/bash
# Walk Mode — local audio cleanup
# Deletes generated MP3s older than 7 days from both the TTS cache and the
# static scene output. Files in static/walk/audio/ are committed to git before
# this runs so they're always recoverable with: git checkout static/walk/audio/
#
# Managed by ~/Library/LaunchAgents/com.japunlocked.cleanup.plist
# To run manually: bash "/Users/robertnelson/jap learn site/tools/walk/cleanup.sh"

REPO="/Users/robertnelson/jap learn site"
CACHE_DIR="$REPO/audio_cache/walk"
AUDIO_DIR="$REPO/static/walk/audio"
DAYS=7
LOG="$HOME/Library/Logs/japunlocked-cleanup.log"

log() { echo "$(date '+%Y-%m-%d %H:%M')  $*" | tee -a "$LOG"; }

log "--- Walk Mode cleanup (files older than ${DAYS} days) ---"

for DIR in "$CACHE_DIR" "$AUDIO_DIR"; do
    if [ ! -d "$DIR" ]; then
        log "skip  $DIR (not found)"
        continue
    fi
    COUNT=$(find "$DIR" -name "*.mp3" -mtime +"$DAYS" | wc -l | tr -d ' ')
    if [ "$COUNT" -eq 0 ]; then
        log "clean $DIR (nothing to remove)"
    else
        find "$DIR" -name "*.mp3" -mtime +"$DAYS" -delete
        log "del   $DIR — removed $COUNT file(s)"
    fi
done

log "done"
