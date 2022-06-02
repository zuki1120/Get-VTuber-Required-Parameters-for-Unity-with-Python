# Get VTuber Required Parameters for Unity with Python Tutorial

使用Python和Unity的VTuber（3D和Live2D）的實現。僅支援CPU的**人臉運動跟蹤，眨眼檢測，虹膜檢測和跟蹤**以及**嘴巴運動跟蹤**。

本專案修改自[VTuber-Python-Unity](https://github.com/mmmmmm44/VTuber-Python-Unity)，有使用Live2D或3D上的相關問題可以查詢該篇之README。

## Usage

```shell
python main.py --output {filename}
```
## How To Use
Clone this project into your directory

```
git clone https://github.com/mmmmmm44/VTuber-Python-Unity.git
cd "VTuber-Python-Unity"
```

Download the unity packages of sample projects of both live2D and unitychan 3D in the link next to: [Dropbox](https://www.dropbox.com/sh/qh7dcqt0z287idt/AACbljJEcD6knM6JL2uojfIaa?dl=0)
### Simple Setup
1. 創建一個空的 Unity 3D 項目

2. 將 Live2D 或 UnityChan3D 包導入您的項目。相應的 SDK 已經包含在內。

Links for both packages (in a zip file): [Dropbox](https://www.dropbox.com/sh/qh7dcqt0z287idt/AACbljJEcD6knM6JL2uojfIaa?dl=0)

1. 運行場景。

2. 在終端運行以下代碼 [括號中的內容是可選的]

```shell
python main.py --output {filename}
```

3. Enjoy

### Custom Setup (For people who want to import their own 3D/ Live2D model)

#### For Live2D model

Video Walkthrough: [Click Me!](https://youtu.be/3pBc9Wkzzos?t=30)

1. Download the Cubism SDK For Unity from this [website](https://www.live2d.com/download/cubism-sdk/) and the sample model used (桃瀬ひより) from this [website](https://www.live2d.com/download/sample-data/)

2. Create an empty Unity 3D project, and import the Cubism SDK. Unzip the model and drag the whole folder to the Project window of the Unity Project.

3. Drag the live2D model's prefab into the scene. Run the scene immediately to allow the model to be shown in Scene and Game window.

4. Adjust the camera's position, background and projection properties. If there are some werid projection problems of the model, changing the projection of the camera from Perspective and Orthographic works for me.

5. Drag the HiyoriController.cs to the Hiyori GameObject. Adjust the parameters in the inspector

6. Run the scene.

7. Run the following code in terminal
[content in the bracket is optional]
```
python main.py --connect [--debug] [--output filename]
```

8. Enjoy

#### For 3D Model (UnityChan)

Video Walkthrough: [Click Me!](https://youtu.be/V6Wd2kPNbPY?t=180)

1. Download the UnityChan model from the [website](https://unity-chan.com/). Go to "Data Download", accept the terms and agreements, and select the first one. Unzip the file.

2. Create an empty Unity 3D Project. Drag the unzipped folder to the Project Window of the project.

3. Go to UnityChan\Prefabs and Drag the "unitychan" prefab into the scene.

4. Adjust the camera's position, background and field of view.

5. Drag the UnityChanControl.cs script onto the prefab. __Change the update mode of the Animator attached to "Animate Physics" and the Controller to UnityChanLocomotions. (Crucial)__ Adjust the variables in the inspector. Disable other attached scripts except AutoBlink and UnityChanController. You may tick the box "is Auto Blink Active" in UnityChanContoller to enable auto blinking (enable AutoBlink script when ticked).

6. Run the scene first

7. Run the following code in terminal
[content in the bracket is optional]
```
python main.py --connect [--debug]
```

8. Enjoy

**Make sure you run the Unity Scene first before running the python script**

*Both the python scripts and the unity project can be exported to .exe, which can be run on other computers.*

## Development Environment
* Python 3.8.5
* Numpy 1.19.2
* OpenCV 4.5.1
* Mediapipe 0.8.9.1

* Unity 2020.3.12f1

(Later version should be supported as well)

*(For Windows, it is recommended to run this project using Anaconda and create a virtual environment before installing such packages.)*

*The whole project is run on a laptop with Intel Core i5-8250U, with 16GB RAM and integrated graphic card only.*

*The same project is tested on a M1 Max device, running in rosetta.*


## References/ Credits

[Detect 468 Face Landmarks in Real-time | OpenCV Python | Computer Vision - Murtaza's Workshop - Robotics and AI](https://youtu.be/V9bzew8A1tc)

[Eye motion tracking - Opencv with Python - Pysoruce](https://youtu.be/kbdbZFT9NQI)

 | Project | Author | LICENSE |
 |:---:|:---:|:---:|
 | [head-pose-estimation](https://github.com/yinguobing/head-pose-estimation) | [Yin Guobing](https://github.com/yinguobing) | [LICENSE](https://github.com/yinguobing/head-pose-estimation/blob/master/LICENSE) |
 | [VTuber_Unity](https://github.com/kwea123/VTuber_Unity) | [AI葵](https://github.com/kwea123) | [LICENSE](https://github.com/kwea123/VTuber_Unity/blob/master/LICENSE) |
 |[VTuber-MomoseHiyori](https://github.com/KennardWang/VTuber-MomoseHiyori) |[KennardWang](https://github.com/KennardWang)|[LICENSE](https://github.com/KennardWang/VTuber-MomoseHiyori/blob/master/LICENSE)|
 |[VTuber-Python-Unity](https://github.com/mmmmmm44/VTuber-Python-Unity)|[mmmmmm44](https://github.com/mmmmmm44)|[LICENSE](https://github.com/mmmmmm44/VTuber-Python-Unity/blob/main/LICENSE)

Hiyori Momose's model
|Position|Creator|
|:---:|:---:|
|Illustration|Kani Biimu [Twitter [@kani_biimu](https://twitter.com/kani_biimu)]|
|Modeling|Live2D Inc.|

## License
MIT

The Unity Chan model in the Unity Packages provided is distributed under Unity-Chan License © Unity Technologies Japan/UCL. A seperate sets of that License is included in UnityAssets/Licenses/UCL2_0
