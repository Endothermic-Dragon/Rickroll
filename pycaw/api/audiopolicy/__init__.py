from ctypes import HRESULT, POINTER, c_float
from ctypes.wintypes import BOOL, DWORD, INT, LPWSTR

from comtypes import COMMETHOD, GUID, IUnknown

from ..audioclient import ISimpleAudioVolume


class IAudioSessionEvents(IUnknown):
    _iid_ = GUID("{073d618c-490a-4f9f-9d18-7bec6fc21121}")
    _methods_ = (
        # HRESULT OnDisplayNameChanged(
        # [in] LPCWSTR NewDisplayName,
        # [in] LPCGUID EventContext);
        COMMETHOD([], HRESULT, "NotImpl1"),
        # HRESULT OnIconPathChanged(
        # [in] LPCWSTR NewIconPath,
        # [in] LPCGUID EventContext);
        COMMETHOD([], HRESULT, "NotImpl2"),
        # HRESULT OnSimpleVolumeChanged(
        # [in] float   NewVolume,
        # [in] BOOL    NewMute,
        # [in] LPCGUID EventContext);
        COMMETHOD(
            [],
            HRESULT,
            "OnSimpleVolumeChanged",
            (["in"], c_float, "NewVolume"),
            (["in"], BOOL, "NewMute"),
            (["in"], POINTER(GUID), "EventContext"),
        ),
        # HRESULT OnChannelVolumeChanged(
        # [in] DWORD    ChannelCount,
        # [in] float [] NewChannelVolumeArray,
        # [in] DWORD    ChangedChannel,
        # [in] LPCGUID  EventContext);
        COMMETHOD([], HRESULT, "NotImpl3"),
        # HRESULT OnGroupingParamChanged(
        # [in] LPCGUID NewGroupingParam,
        # [in] LPCGUID EventContext);
        COMMETHOD([], HRESULT, "NotImpl4"),
        # HRESULT OnStateChanged(
        # AudioSessionState NewState);
        COMMETHOD([], HRESULT, "OnStateChanged", (["in"], DWORD, "NewState")),
        # HRESULT OnSessionDisconnected(
        # [in] AudioSessionDisconnectReason DisconnectReason);
        COMMETHOD(
            [], HRESULT, "OnSessionDisconnected", (["in"], DWORD, "DisconnectReason")
        ),
    )


class IAudioSessionControl(IUnknown):
    _iid_ = GUID("{F4B1A599-7266-4319-A8CA-E70ACB11E8CD}")
    _methods_ = (
        # HRESULT GetState ([out] AudioSessionState *pRetVal);
        COMMETHOD([], HRESULT, "GetState", (["out"], POINTER(DWORD), "pRetVal")),
        # HRESULT GetDisplayName([out] LPWSTR *pRetVal);
        COMMETHOD([], HRESULT, "GetDisplayName", (["out"], POINTER(LPWSTR), "pRetVal")),
        # HRESULT SetDisplayName(
        # [in] LPCWSTR Value,
        # [in] LPCGUID EventContext);
        COMMETHOD([], HRESULT, "NotImpl2"),
        # HRESULT GetIconPath([out] LPWSTR *pRetVal);
        COMMETHOD([], HRESULT, "NotImpl3"),
        # HRESULT SetIconPath(
        # [in] LPCWSTR Value,
        # [in] LPCGUID EventContext);
        COMMETHOD([], HRESULT, "NotImpl4"),
        # HRESULT GetGroupingParam([out] GUID *pRetVal);
        COMMETHOD([], HRESULT, "NotImpl5"),
        # HRESULT SetGroupingParam(
        # [in] LPCGUID Grouping,
        # [in] LPCGUID EventContext);
        COMMETHOD([], HRESULT, "NotImpl6"),
        # HRESULT RegisterAudioSessionNotification(
        # [in] IAudioSessionEvents *NewNotifications);
        COMMETHOD(
            [],
            HRESULT,
            "RegisterAudioSessionNotification",
            (["in"], POINTER(IAudioSessionEvents), "NewNotifications"),
        ),
        # HRESULT UnregisterAudioSessionNotification(
        # [in] IAudioSessionEvents *NewNotifications);
        COMMETHOD(
            [],
            HRESULT,
            "UnregisterAudioSessionNotification",
            (["in"], POINTER(IAudioSessionEvents), "NewNotifications"),
        ),
    )


class IAudioSessionControl2(IAudioSessionControl):
    _iid_ = GUID("{BFB7FF88-7239-4FC9-8FA2-07C950BE9C6D}")
    _methods_ = (
        # HRESULT GetSessionIdentifier([out] LPWSTR *pRetVal);
        COMMETHOD(
            [], HRESULT, "GetSessionIdentifier", (["out"], POINTER(LPWSTR), "pRetVal")
        ),
        # HRESULT GetSessionInstanceIdentifier([out] LPWSTR *pRetVal);
        COMMETHOD(
            [],
            HRESULT,
            "GetSessionInstanceIdentifier",
            (["out"], POINTER(LPWSTR), "pRetVal"),
        ),
        # HRESULT GetProcessId([out] DWORD *pRetVal);
        COMMETHOD([], HRESULT, "GetProcessId", (["out"], POINTER(DWORD), "pRetVal")),
        # HRESULT IsSystemSoundsSession();
        COMMETHOD([], HRESULT, "IsSystemSoundsSession"),
        COMMETHOD([], HRESULT, "SetDuckingPreferences", (["in"], BOOL, "optOut")),
    )


class IAudioSessionEnumerator(IUnknown):
    _iid_ = GUID("{E2F5BB11-0570-40CA-ACDD-3AA01277DEE8}")
    _methods_ = (
        # HRESULT GetCount([out] int *SessionCount);
        COMMETHOD([], HRESULT, "GetCount", (["out"], POINTER(INT), "SessionCount")),
        # HRESULT GetSession(
        # [in] int SessionCount,
        # [out] IAudioSessionControl **Session);
        COMMETHOD(
            [],
            HRESULT,
            "GetSession",
            (["in"], INT, "SessionCount"),
            (["out"], POINTER(POINTER(IAudioSessionControl)), "Session"),
        ),
    )


class IAudioSessionManager(IUnknown):
    _iid_ = GUID("{BFA971F1-4d5e-40bb-935e-967039bfbee4}")
    _methods_ = (
        # HRESULT GetAudioSessionControl(
        # [in] LPCGUID AudioSessionGuid,
        # [in] DWORD StreamFlags,
        # [out] IAudioSessionControl **SessionControl);
        COMMETHOD([], HRESULT, "NotImpl1"),
        # HRESULT GetSimpleAudioVolume(
        # [in] LPCGUID AudioSessionGuid,
        # [in] DWORD CrossProcessSession,
        # [out] ISimpleAudioVolume **AudioVolume);
        COMMETHOD(
            [],
            HRESULT,
            "GetSimpleAudioVolume",
            (["in"], POINTER(GUID), "AudioSessionGuid"),
            (["in"], DWORD, "CrossProcessSession"),
            (["out"], POINTER(POINTER(ISimpleAudioVolume)), "AudioVolume"),
        ),
    )


class IAudioSessionNotification(IUnknown):
    _iid_ = GUID("{8aad9bb7-39e1-4c62-a3ab-ff6e76dcf9c8}")
    _methods_ = (
        # HRESULT OnSessionCreated(
        # ['in'] IAudioSessionControl *NewSession
        # );
        COMMETHOD(
            [],
            HRESULT,
            "OnSessionCreated",
            (["in"], POINTER(IAudioSessionControl), "NewSession"),
        ),
    )


class IAudioSessionManager2(IAudioSessionManager):
    _iid_ = GUID("{77aa99a0-1bd6-484f-8bc7-2c654c9a9b6f}")
    _methods_ = (
        # HRESULT GetSessionEnumerator(
        # [out] IAudioSessionEnumerator **SessionList);
        COMMETHOD(
            [],
            HRESULT,
            "GetSessionEnumerator",
            (["out"], POINTER(POINTER(IAudioSessionEnumerator)), "SessionList"),
        ),
        # HRESULT RegisterSessionNotification(
        # IAudioSessionNotification *SessionNotification);
        COMMETHOD(
            [],
            HRESULT,
            "RegisterSessionNotification",
            (["in"], POINTER(IAudioSessionNotification), "SessionNotification"),
        ),
        # HRESULT UnregisterSessionNotification(
        # IAudioSessionNotification *SessionNotification);
        COMMETHOD(
            [],
            HRESULT,
            "UnregisterSessionNotification",
            (["in"], POINTER(IAudioSessionNotification), "SessionNotification"),
        ),
        # HRESULT RegisterDuckNotification(
        # LPCWSTR SessionID,
        # IAudioVolumeDuckNotification *duckNotification);
        COMMETHOD([], HRESULT, "NotImpl1"),
        # HRESULT UnregisterDuckNotification(
        # IAudioVolumeDuckNotification *duckNotification);
        COMMETHOD([], HRESULT, "NotImpl2"),
    )
