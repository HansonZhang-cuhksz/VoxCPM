# from huggingface_hub import snapshot_download

# # Choose where you want the model files to be stored
# dest = r".\\VoxCPM-1.5"

# snapshot_download(
#     repo_id="openbmb/VoxCPM-1.5",
#     local_dir=dest,
#     local_dir_use_symlinks=False,  # recommended on Windows
# )

from modelscope import snapshot_download

snapshot_download("iic/speech_zipenhancer_ans_multiloss_16k_base", cache_dir=".\\modelscope")
snapshot_download("iic/SenseVoiceSmall", cache_dir=".\\modelscope") 