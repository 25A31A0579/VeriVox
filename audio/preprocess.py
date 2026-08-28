import numpy as np
import librosa


def preprocess_audio(file_path):
    """
    Load and preprocess audio for Wav2Vec2.

    Returns:
        np.ndarray: 1-D float32 mono waveform at 16 kHz.
    """

    waveform, sample_rate = librosa.load(
        file_path,
        sr=16000,
        mono=True
    )

    waveform = np.asarray(waveform, dtype=np.float32)

    return waveform
