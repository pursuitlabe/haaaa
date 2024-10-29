1.环境配置：
Python >= 3.6
PyTorch >= 1.1.0
PyYAML, tqdm, tensorboardX
2.数据位置：
./data/uav
下载数据集链接: https://pan.baidu.com/s/1Sr_IJ1pLUyJA8wKdn0N2jw 提取码: haaa
3.运行方式：
训练：
joint训练：python main.py --config config/uav/default.yaml --work-dir work_dir/uav/csub/ctrgcn --device 0
bone训练：python main.py --config config/uav/default.yaml --work-dir work_dir/uav/csub/bone --device 0
测试：
joint 测试b：
python main.py --config work_dir/uav/csub/ctrgcn/config.yaml --work-dir work_dir/uav/csub/joint --phase test --save-score True --weights work_dir/uav/csub/ctrgcn/runs-55-28215.pt --device 0
bone 测试b：
python main.py --config work_dir/uav/csub/bone/config.yaml --work-dir work_dir/uav/csub/bone_test --phase test --save-score True --weights work_dir/uav/csub/bone/runs-56-28728.pt --device 0
