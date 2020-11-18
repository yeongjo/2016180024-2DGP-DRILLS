#pragma once
#include "stdafx.h"

#define MAP_WIDTH 1920
#define MAP_HEIGHT 1080
#define MAP_HALF_WIDTH MAP_WIDTH/2
#define MAP_HALF_HEIGHT MAP_HEIGHT/2
#define WALLSIZE 400
#define FurnitureImgWidth 50

class Player;

class Obj {
public:
	int id = -1;
	vec2 pos;

	Obj() {
		id = totalObjCnt++;
	}
	virtual ~Obj(){}
private:
	static int totalObjCnt;
};

class InteractObj : public Obj
{
	float interactDistance = 150;
protected:
	virtual void OnInteracted(Obj* other) = 0;
public:
	InteractObj();
	int Interact(Obj* other);
};

class InteractObjManager {
public:
	static vector<InteractObj*> interactObjs;

	static int Interact(Obj* other);
};

class Stair : public Obj {
public:
	Stair* otherStair = nullptr; // 가운데 건물이 맞닿는지점 서로 연결된 계단 포인터

	Stair(vec2 pos, Stair* other);

	void SetOtherStair(Stair* other);
};

class Furniture : public InteractObj {
protected:
	// 상호작용 한 플레이어에게 점수 추가로 줌
	void OnInteracted(Obj* other) override;
public:
	Player* interactPlayer = nullptr;
};

class Building
{
	static constexpr float EACH_FLOOR_HEIGHT_OFFSET_PER_BUILDING[3] = { 218, -139, -500 };

public:
	vector<Stair> stairs;
	vector<Furniture> furnitures;

	void Init();

	// 몇 층의 바닥의 높이가 얼마인지 받는 함수
	static float CalculateFloorHeight(int floor);
private:
	// 계단과 충돌검사를 위해 계단 만듬
	void CreateStairs();

	void CreateFurnitures();
};

