# Usage of `REINFORCEpy`

Initially I ran

```bash
conda create -n reinforce-py python=3.11.7 -y
conda activate reinforce-py

conda install pytorch::pytorch torchvision torchaudio -c pytorch -y

```

Create the environment using

```bash
conda env create -f environment.yml
```

Run the experiments via

```bash
python main.py \
    --verbose=1
    --episodes=10 \
    --timesteps=1000 \
```
