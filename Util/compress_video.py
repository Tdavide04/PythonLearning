import subprocess
import os

def get_video_duration(input_path):
    """Returns the duration of the video in seconds using ffprobe."""
    result = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", input_path],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    return float(result.stdout.strip())

def compress_video(input_path, output_path, target_size_mb, remove_audio=False):
    """
    Compresses a video to a target size (in MB).
    Optionally removes audio.
    """
    # Calculate target bitrate in kbps
    duration = get_video_duration(input_path)
    # convert MB to bits: MB * 8e6 bits
    target_bitrate = (target_size_mb * 8 * 1024 * 1024) / duration
    # ffmpeg expects video bitrate in kbps
    vb_kbps = int(target_bitrate / 1000)

    # Build ffmpeg command
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-c:v", "libx264",
        "-b:v", f"{vb_kbps}k",
        "-preset", "medium"
    ]
    if remove_audio:
        cmd += ["-an"]
    else:
        # Copy audio to keep original quality
        cmd += ["-c:a", "copy"]
    cmd += [output_path]

    print("Running ffmpeg command:")
    print(" ".join(cmd))
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Compress video to a target size.")
    parser.add_argument("input", help="Path to input video file")
    parser.add_argument("output", help="Path for output compressed video")
    parser.add_argument("--size", type=float, default=10.0, help="Target size in MB (default: 10)")
    parser.add_argument("--remove-audio", action="store_true", help="Remove audio track if set")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: Input file {args.input} does not exist.")
    else:
        compress_video(args.input, args.output, args.size, args.remove_audio)

# Save this script as /mnt/data/compress_video.py