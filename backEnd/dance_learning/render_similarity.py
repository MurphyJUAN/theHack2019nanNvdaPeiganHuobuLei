# -*- Encoding:UTF-8 -*- #

import sys
import os
from glob import glob
import cPickle as pickle
import numpy as np
from opendr.renderer import ColoredRenderer
from opendr.lighting import LambertianPointLight
from opendr.camera import ProjectPoints
from smpl_webuser.serialization import load_model
from matplotlib import pyplot
import cv2
import math

colors = {
    'pink': [.7, .7, .9],
    'neutral': [.9, .9, .8],
    'capsule': [.7, .75, .5],
    'yellow': [.5, .7, .75],
}

def _create_renderer(w=640,
                     h=480,
                     rt=np.array([0, 0, 0]),
                     t=np.zeros(3),
                     f=None,
                     c=None,
                     k=None,
                     near=.5,
                     far=10.):

    f = np.array([w, w]) / 2. if f is None else f
    c = np.array([w, h]) / 2. if c is None else c
    k = np.zeros(5) if k is None else k

    rn = ColoredRenderer()

    rn.camera = ProjectPoints(rt=rt, t=t, f=f, c=c, k=k)
    rn.frustum = {'near': near, 'far': far, 'height': h, 'width': w}
    return rn


def _rotateY(points, angle):
    """Rotate the points by a specified angle."""
    ry = np.array([
        [np.cos(angle), 0., np.sin(angle)], [0., 1., 0.],
        [-np.sin(angle), 0., np.cos(angle)]
    ])
    return np.dot(points, ry)


def simple_renderer(rn, verts, faces, yrot=np.radians(120)):

    # Rendered model color
    color = colors['pink']

    rn.set(v=verts, f=faces, vc=color, bgcolor=np.ones(3))

    albedo = rn.vc

    # Construct Back Light (on back right corner)
    rn.vc = LambertianPointLight(
        f=rn.f,
        v=rn.v,
        num_verts=len(rn.v),
        light_pos=_rotateY(np.array([-200, -100, -100]), yrot),
        vc=albedo,
        light_color=np.array([1, 1, 1]))

    # Construct Left Light
    rn.vc += LambertianPointLight(
        f=rn.f,
        v=rn.v,
        num_verts=len(rn.v),
        light_pos=_rotateY(np.array([800, 10, 300]), yrot),
        vc=albedo,
        light_color=np.array([1, 1, 1]))

    # Construct Right Light
    rn.vc += LambertianPointLight(
        f=rn.f,
        v=rn.v,
        num_verts=len(rn.v),
        light_pos=_rotateY(np.array([-500, 500, 1000]), yrot),
        vc=albedo,
        light_color=np.array([.7, .7, .7]))

    return rn.r


def get_alpha(imtmp, bgval=1.):
    h, w = imtmp.shape[:2]
    alpha = (~np.all(imtmp == bgval, axis=2)).astype(imtmp.dtype)

    b_channel, g_channel, r_channel = cv2.split(imtmp)

    im_RGBA = cv2.merge(
        (b_channel, g_channel, r_channel, alpha.astype(imtmp.dtype)))
    return im_RGBA


def render_model(verts, faces, w, h, rt, t, f, near=0.5, far=100, img=None):
    rn = _create_renderer(
        w=w, h=h, near=near, far=far, rt=rt, t=t, f=f)
    # Uses img as background, otherwise white background.
    if img is not None:
        rn.background_image = img / 255. if img.max() > 1 else img


    imtmp = simple_renderer(rn, verts, faces)

    # If white bg, make transparent.
    if img is None:
        imtmp = get_alpha(imtmp)

    return imtmp

def similarity(res, res2, ind, ind2, img2, op_joints, op_joints2): # ind는 model 인덱스, ind2는 compare 인덱스
	result=0
	indiSimil=np.zeros(12)
	indiResult=np.zeros(12)
	index=0 # 관절별 인덱스
	#vectors = [60, 54, 48, 63, 57, 51, 21, 12, 3, 24, 15, 6]
	vectors = [24,15,6,3,12,21,63,57,51,48,54,60]
	distance = [int(op_joints2[ind2][13][0]-op_joints[ind][13][0]),int(op_joints2[ind2][13][1]-op_joints[ind][13][1])]
	for vector in vectors:
		for i in range(3):
			indiResult[index]+=abs(res['pose'][vector+i]-res2['pose'][vector+i])
		indiSimil[index]=1 / (1+indiResult[index])
		result+=indiResult[index]
		indiSimil[index]*=100
		if((indiSimil[index]<80 and index >=7)or(indiSimil[index]<60)):
			cv2.arrowedLine(img2,(int(op_joints2[ind2][index][0]),int(op_joints2[ind2][index][1])),(int(op_joints[ind][index][0])+distance[0],int(op_joints[ind][index][1])+distance[1]),(0,0,128),1)
			cv2.circle(img2,(int(op_joints2[ind2][index][0]),int(op_joints2[ind2][index][1])),10,(0,0,255))
			print(str(vector)+"wrong")
		index+=1

	res = sum(indiSimil)
	res /= len(indiSimil)
	return res

def similarity2(res, res2):
	vectors = [[60, 54], [54, 48], [63, 57], [57, 51], [21, 12], [12, 3], [24, 15], [15,6]]
	similarity = 0.0
	result = []
	for vector in vectors:
		v1 = []
		v2 = []
		for i in range(3):
			t1 = res['pose'][vector[0] + i] - res['pose'][vector[1] + i]
			t2 = res2['pose'][vector[0] + i] - res2['pose'][vector[1] + i]
			v1.append(t1)
			v2.append(t2)
		np_v1 = np.array(v1)
		np_v2 = np.array(v2)
		cos_theta = sum(np_v1 * np_v2) / math.sqrt(sum(np_v1 ** 2) * sum(np_v2 ** 2))
		rad = abs(math.acos(cos_theta))
		if rad > math.pi:
			rad -= math.pi
		result.append(1 - rad / math.pi)
		print(str(1-rad/math.pi))
	similarity = sum(result) / len(result) * 100
	print(str(similarity)+"%")
